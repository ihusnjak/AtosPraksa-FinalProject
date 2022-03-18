package hr.atos.praksa.tictactoecpp;

import android.content.Intent;
import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;

import hr.atos.praksa.tictactoecpp.adapters.MatchesAdapter;
import hr.atos.praksa.tictactoecpp.listeners.OnMatchClickListener;
import hr.atos.praksa.tictactoecpp.listeners.UiListener;
import hr.atos.praksa.tictactoecpp.model.Match;
import hr.atos.praksa.tictactoecpp.retrofit.RetrofitInstance;

public class MatchHistoryActivity extends AppCompatActivity implements OnMatchClickListener, UiListener {

    private RecyclerView recyclerView;
    private MatchesAdapter matchesAdapter;
    private ArrayList<Match> matchesList;
    private RetrofitInstance retrofitInstance;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_match_history);

        setupUiElements();

        retrofitInstance = RetrofitInstance.getInstance();
        retrofitInstance.setListener(this);
        retrofitInstance.getAllMatchesFromServer();


        matchesList = new ArrayList<>();
    }

    private void setupUiElements(){
        recyclerView = findViewById(R.id.rv_matchHistory);
        recyclerView.setHasFixedSize(true);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
    }

    @Override
    public void onMatchClick(int position) {
        Intent intent = new Intent(this, MatchDetailsActivity.class);
        Match match = matchesList.get(position);
        intent.putExtra("match", match);

        startActivity(intent);
    }

    @Override
    public void onModificationPerformed(ArrayList<Match> matches) {
        this.matchesList.addAll(matches);
        matchesAdapter = new MatchesAdapter(MatchHistoryActivity.this, matchesList, this);
        recyclerView.setAdapter(matchesAdapter);
        matchesAdapter.setOnMatchClickListener(MatchHistoryActivity.this);
    }
}