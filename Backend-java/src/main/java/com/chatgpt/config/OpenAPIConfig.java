package com.chatgpt.config;

import java.util.List;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Contact;
import io.swagger.v3.oas.models.info.Info;
import io.swagger.v3.oas.models.info.License;
import io.swagger.v3.oas.models.security.SecurityScheme;
import io.swagger.v3.oas.models.servers.Server;

@Configuration
public class OpenAPIConfig {

  @Value("${inevitables.openapi.dev-url}")
  private String devUrl;

  @Value("${inevitables.openapi.prod-url}")
  private String prodUrl;
  
//  @Value("${inevitables.openapi.api-key}")
//  private String apiKey;

  @Bean
  public OpenAPI myOpenAPI() {
    Server devServer = new Server();
    devServer.setUrl(devUrl);
    devServer.setDescription("Server URL in Development environment");

    Server prodServer = new Server();
    prodServer.setUrl(prodUrl);
    prodServer.setDescription("Server URL in Production environment");

    Contact contact = new Contact();
    contact.setEmail("inevitables@gmail.com");
    contact.setName("Inevitables");
    contact.setUrl("https://www.Inevitables.com");
    

    License mitLicense = new License().name("MIT License").url("https://choosealicense.com/licenses/mit/");

    Info info = new Info()
        .title("Dragon Tales API Documentation")
        .version("1.0")
        .contact(contact)
        .description("This API exposes endpoints to manipulate Chatgpt reponses and save to Atlas DB.").termsOfService("https://www.Inevitables.com/terms")
        .license(mitLicense);
    
    
    return new OpenAPI().info(info).servers(List.of(devServer, prodServer));
  }
}