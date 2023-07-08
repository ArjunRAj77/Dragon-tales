package com.chatgpt.requestDto;

import java.util.List;

import com.chatgpt.requestResponseCommons.Message;

public class ChatGPTRequest {

	private String model;
	private List<Message> messages;
	private Integer max_tokens;

	public String getModel() {
		return model;
	}

	public void setModel(String model) {
		this.model = model;
	}

	public List<Message> getMessages() {
		return messages;
	}

	public void setMessages(List<Message> messages) {
		this.messages = messages;
	}

	public Integer getMax_tokens() {
		return max_tokens;
	}

	public void setMax_tokens(Integer max_tokens) {
		this.max_tokens = max_tokens;
	}

}
