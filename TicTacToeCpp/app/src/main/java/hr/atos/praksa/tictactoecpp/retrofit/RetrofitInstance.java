package hr.atos.praksa.tictactoecpp.retrofit;

import android.util.Log;

import java.util.ArrayList;

import hr.atos.praksa.tictactoecpp.listeners.UiListener;
import hr.atos.praksa.tictactoecpp.model.Match;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class RetrofitInstance {

    private static final String TAG = "RetrofitInstance";
    private ArrayList<Match> matchesList = new ArrayList<>();
    private static RetrofitInstance instance;
    private UiListener uiListener;

    private RetrofitInstance(){}

    public static RetrofitInstance getInstance(){
        if (instance == null) {
            instance = new RetrofitInstance();
        }
        return instance;
    }

    public void setListener(UiListener uiListener){
        this.uiListener = uiListener;
    }

    public void getAllMatchesFromServer(){
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://188.166.133.147:8081")
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        MatchesApi matchesApi = retrofit.create(MatchesApi.class);

        Call<ArrayList<Match>> matches = matchesApi.getMatches();

        matches.enqueue(new Callback<ArrayList<Match>>() {
            @Override
            public void onResponse(Call<ArrayList<Match>> call, Response<ArrayList<Match>> response) {
                if(response.isSuccessful()){
                    Log.d(TAG, "onResponse: success");
                    ArrayList<Match> matches = response.body();
                    if(!matches.isEmpty()) {
                        matchesList.clear();
                        matchesList.addAll(matches);
                        Log.d(TAG, "in func:" + matchesList.toString());
                        notifyUi(matchesList);
                    }
                }
                else{
                    Log.d(TAG, "onResponse: response fail");
                }
            }

            @Override
            public void onFailure(Call<ArrayList<Match>> call, Throwable t) {
                Log.e(TAG, "onFailure: failed" + t.getMessage());
            }
        });
    }

    public void notifyUi(ArrayList<Match> matches){
        if(uiListener != null){
            uiListener.onModificationPerformed(matches);
        }
    }
}
