package hr.atos.praksa.tictactoecpp.retrofit;

import java.util.ArrayList;

import hr.atos.praksa.tictactoecpp.model.Match;
import retrofit2.Call;
import retrofit2.http.GET;

public interface MatchesApi {

    @GET("/games")
    Call<ArrayList<Match>> getMatches();
}
