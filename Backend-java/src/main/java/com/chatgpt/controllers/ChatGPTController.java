package com.chatgpt.controllers;

import java.util.List;
import java.util.Optional;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.chatgpt.requestDto.ChatBotInputRequest;
import com.chatgpt.requestDto.FavDto;
import com.chatgpt.requestDto.Story;
import com.chatgpt.services.ChatGPTService;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.tags.Tag;

@RestController
@RequestMapping("/api/v1")
@Tag(name = "Dragon Tales", description = "Tales management APIs")
public class ChatGPTController {

	private ChatGPTService chatGPTService;

	public ChatGPTController(ChatGPTService chatGPTService, ObjectMapper objectMapper) {
		this.chatGPTService = chatGPTService;
	}

	@Operation(summary = "Generate Story", description = "Use this api to generete GPT responses", tags = {
			"Generate story with user prompt" })
	@ApiResponses()
	@PostMapping(value = "/chat")
	public Story processInputRequest(@RequestBody ChatBotInputRequest chatbotInputRequest)
			throws JsonMappingException, JsonProcessingException {
		return chatGPTService.getChatCPTResponse(chatbotInputRequest.getMessage());

	}

	@Operation(summary = "Retrieve Every Story", description = "Get every story to pupulate in stoyhub pane", tags = {
			" Get all Story" })
	@ApiResponses()
	@GetMapping("/")
	public List<Story> getAllGeneratedStory() {
		return chatGPTService.getAllGenerated();
	}

	@Operation(summary = "Retrieve each story by id", description = "Use this API to persist data in the homescreen even when the user reloads.", tags = {
			" Get Story by Id" })
	@ApiResponses()
	@GetMapping("/{id}")
	public Optional<Story> getGeneratedStoryById(@PathVariable("id") String id) {
		return chatGPTService.getStory(id);
	}

	@Operation(summary = "Update User Favorite to true", description = "By default everystory is created with false as favorite ,use this api to change fav value ", tags = {
			" Mark as Favorite" })
	@ApiResponses()
	@PutMapping("/fav")
	public void updateFavorite(@RequestBody  FavDto fav) {	
		chatGPTService.updateFavorite(fav.getId(),fav.getFavorite());
	}

}
