package com.chatgpt.Repository;

import org.springframework.data.mongodb.repository.MongoRepository;
import com.chatgpt.requestDto.Story;

public interface StoryRepositoy extends MongoRepository<Story, String> {
	
	// void saveFavoriteStatusById(String id, String favorite);

}
