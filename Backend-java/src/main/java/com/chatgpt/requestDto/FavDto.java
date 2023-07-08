package com.chatgpt.requestDto;

public class FavDto {

	private String id;
	private String favorite;

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getFavorite() {
		return favorite;
	}

	public void setFavorite(String favorite) {
		this.favorite = favorite;
	}

	public FavDto(String id, String favorite) {
		super();
		this.id = id;
		this.favorite = favorite;
	}

}
