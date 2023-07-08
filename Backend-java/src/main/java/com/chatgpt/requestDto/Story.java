package com.chatgpt.requestDto;

import java.util.Arrays;
import java.util.List;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "story")
public class Story {

	@Id
	private String id;

	private String Story;

	private String title;

	private List<String> genres;

	private String favorite;

	public Story(String title, String genre, String storyBody) {
		this.title = title;
		this.genres = Arrays.asList(genre.split("/"));
		this.Story = storyBody;
		this.favorite = "false";
	}


	public String getFavorite() {
		return favorite;
	}


	public void setFavorite(String favorite) {
		this.favorite = favorite;
	}



	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public List<String> getGenres() {
		return genres;
	}

	public void setGenres(List<String> genres) {
		this.genres = genres;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getStory() {
		return Story;
	}

	public void setStory(String story) {
		Story = story;
	}

	public Story(String id, String story) {
		super();
		this.id = id;
		Story = story;
	}

	public Story() {
		// TODO Auto-generated constructor stub
	}

}
