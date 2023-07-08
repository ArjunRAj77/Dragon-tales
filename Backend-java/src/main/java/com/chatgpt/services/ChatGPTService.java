package com.chatgpt.services;

import java.util.List;
import java.util.Optional;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import com.chatgpt.Repository.StoryRepositoy;
import com.chatgpt.requestDto.ChatGPTRequest;
import com.chatgpt.requestDto.Story;
import com.chatgpt.requestResponseCommons.ChatMessageDTO;
import com.chatgpt.requestResponseCommons.Message;
import com.chatgpt.responseDto.ChatGPTResponse;
import com.chatgpt.responseDto.Choice;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonMappingException;

@Service
public class ChatGPTService {

	@Value("${openai.api.key}")
	private String apiKey;

	private static final String OPEN_AI_CHAT_ENDPOINT = "https://api.openai.com/v1/chat/completions";

	private RestTemplate restTemplate;

	@Autowired
	private StoryRepositoy storyRepository;

	public ChatGPTService(RestTemplate restTemplate) {
		this.restTemplate = restTemplate;
	}

	public Story getChatCPTResponse(String prompt) throws JsonMappingException, JsonProcessingException {

		org.slf4j.Logger logger = LoggerFactory.getLogger(ChatGPTService.class);
		HttpHeaders headers = new HttpHeaders();
		headers.setContentType(MediaType.APPLICATION_JSON);
		headers.set("Authorization", "Bearer " + apiKey);

		ChatGPTRequest chatGPTRequest = new ChatGPTRequest();
		chatGPTRequest.setModel("gpt-3.5-turbo");
		chatGPTRequest.setMessages(List.of(new Message("user", prompt)));
		chatGPTRequest.setMax_tokens(3000);

		RestTemplate restTemplate = new RestTemplate();
		HttpEntity<ChatGPTRequest> request = new HttpEntity<>(chatGPTRequest, headers);

		ChatGPTResponse response = restTemplate.postForObject(OPEN_AI_CHAT_ENDPOINT, request, ChatGPTResponse.class);

		List<Choice> choices = response.getChoices();
		Message message = choices.get(0).getMessage();
		ChatMessageDTO chatMessageDTO = new ChatMessageDTO();
		String jsonResponse = chatMessageDTO.setMessage(message.getContent());
		logger.info(jsonResponse);
		String titleRegex = "Title: (.+)";
		String genreRegex = "Genre: (.+)";

		Pattern titlePattern = Pattern.compile(titleRegex);
		Pattern genrePattern = Pattern.compile(genreRegex);
		Matcher titleMatcher = titlePattern.matcher(jsonResponse);
		Matcher genreMatcher = genrePattern.matcher(jsonResponse);

		String title = "";
		String genre = "";

		if (titleMatcher.find()) {
			title = titleMatcher.group(1);
		}

		if (genreMatcher.find()) {
			genre = genreMatcher.group(1);
		}

		System.out.println("Title: " + title);
		System.out.println("Genre: " + genre);

		String storyBody = jsonResponse.replaceAll(titleRegex + "|" + genreRegex, "").trim();

		Story story = new Story(title, genre, storyBody);
		story.setStory(storyBody);
		story.setTitle(title);
		storyRepository.save(story);
		return story;

	}

	public List<Story> getAllGenerated() {
		return storyRepository.findAll();
	}

	public Optional<Story> getStory(String id) {
		return storyRepository.findById(id);
	}

	public void updateFavorite(String Id , String favorite) {
		Story item = storyRepository.findById(Id)
				.orElseThrow(() -> new IllegalArgumentException("Item not found with id: " + Id));	
		item.setFavorite(favorite);	
		storyRepository.save(item);
	}

}
