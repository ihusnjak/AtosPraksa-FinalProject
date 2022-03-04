package com.example.clientserverdemo;

import android.util.Log;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class Logic {
    private static final String TAG = "Logic";

    public static Logic logic;
    private UiListener uiListener;

    private Logic() {

    }

    public static Logic getInstance() {
        if (logic == null) {
            logic = new Logic();
        }
        return logic;
    }

    public void setListener(UiListener uiListener) {
        this.uiListener = uiListener;
    }

    public void performCalculation(String fullName) {
        //contact server
        String[] parts = fullName.split(" ");
        postToServer(parts[0], parts[1]);
    }

    private void postToServer(String firstName, String lastName) {
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://188.166.133.147:8001/")
                .addConverterFactory(GsonConverterFactory.create())
                .build();
        PersonApi personApi = retrofit.create(PersonApi.class);
        Call<Person> person = personApi.postUserInfo(new Person(firstName, lastName));

        person.enqueue(new Callback<Person>() {
            @Override
            public void onResponse(Call<Person> call, Response<Person> response) {
                if (response.isSuccessful()) {
                    Log.d(TAG, "onResponse: success");
                    Person person = response.body();
                    if(person != null) {
                        notifyUI(person.getFirstName(), person.getLastName());
                    }
                } else {
                    Log.d(TAG,
                            "onResponse: response not successful " + response.code());
                }
            }

            @Override
            public void onFailure(Call<Person> call, Throwable t) {
                Log.e(TAG, "onFailure: failed" + t.getMessage());

            }
        });


    }

    public void notifyUI(String firstName, String lastName) {
        if (uiListener != null) {
            uiListener.onModificationPerformed(firstName, lastName);
        }
    }
}
