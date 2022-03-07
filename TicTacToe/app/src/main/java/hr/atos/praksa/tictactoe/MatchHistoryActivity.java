package hr.atos.praksa.tictactoe;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;

import java.util.ArrayList;

import hr.atos.praksa.tictactoe.adapters.MatchesAdapter;
import hr.atos.praksa.tictactoe.model.Match;

public class MatchHistoryActivity extends AppCompatActivity {

    private RecyclerView recyclerView;
    private MatchesAdapter matchesAdapter;
    private ArrayList<Match> matchArrayList;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_match_history);

        recyclerView = findViewById(R.id.rv_matchHistory);
        recyclerView.setHasFixedSize(true);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        matchArrayList = new ArrayList<>();

        matchArrayList.add(new Match("pero", "ivan", "ivan"));
        matchArrayList.add(new Match("pero", "ivan", "pero"));
        matchArrayList.add(new Match("iva", "ivan", "ivan"));
        matchArrayList.add(new Match("ivica", "ivan", "ivica"));
        matchArrayList.add(new Match("marko", "ivan", "tie"));
        matchArrayList.add(new Match("petar", "ivan", "ivan"));
        matchArrayList.add(new Match("ante", "ivan", "tie"));
        matchArrayList.add(new Match("anto", "ivan", "anto"));
        matchArrayList.add(new Match("kristijan", "ivan", "ivan"));
        matchArrayList.add(new Match("pero", "ivan", "tie"));

        matchesAdapter = new MatchesAdapter(MatchHistoryActivity.this, matchArrayList);
        recyclerView.setAdapter(matchesAdapter);
    }
}