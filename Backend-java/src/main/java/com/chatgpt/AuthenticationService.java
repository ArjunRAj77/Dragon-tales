//package com.chatgpt;
//
//import org.springframework.security.authentication.BadCredentialsException;
//import org.springframework.security.core.Authentication;
//import org.springframework.security.core.authority.AuthorityUtils;
//
//import jakarta.servlet.http.HttpServletRequest;
//
//public class AuthenticationService {
//
//    private static final String AUTH_TOKEN_HEADER_NAME = "API-KEY";
//    private static final String AUTH_TOKEN = "NvKX1N3YX13vr63u5UMVEtAWZ11Pj0CoBcifl5vQsA8Y90XbiTevHZze93wp75j3";
//
//    public static Authentication getAuthentication(HttpServletRequest request) {
//        String apiKey = request.getHeader(AUTH_TOKEN_HEADER_NAME);
//        if (apiKey == null || !apiKey.equals(AUTH_TOKEN)) {
//            throw new BadCredentialsException("Invalid API Key");
//        }
//
//        return new ApiKeyAuthentication(apiKey, AuthorityUtils.NO_AUTHORITIES);
//    }
//}
