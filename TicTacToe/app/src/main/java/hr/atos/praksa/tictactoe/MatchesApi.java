package hr.atos.praksa.tictactoe;

import java.util.ArrayList;

import hr.atos.praksa.tictactoe.model.Match;
import retrofit2.Call;
import retrofit2.http.GET;

public interface MatchesApi {

    @GET(".")
    Call<ArrayList<Match>> getMatches();
}
