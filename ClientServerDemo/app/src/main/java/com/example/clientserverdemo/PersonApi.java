package com.example.clientserverdemo;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;

public interface PersonApi {

    @POST("echo")
    Call<Person> postUserInfo(@Body Person person);
}
