package hr.atos.praksa.tictactoe;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.content.Intent;
import android.os.Bundle;

import java.util.ArrayList;

import hr.atos.praksa.tictactoe.adapters.MatchesAdapter;
import hr.atos.praksa.tictactoe.listeners.OnMatchClickListener;
import hr.atos.praksa.tictactoe.model.Match;
import hr.atos.praksa.tictactoe.model.Move;

public class MatchHistoryActivity extends AppCompatActivity implements OnMatchClickListener {

    private RecyclerView recyclerView;
    private MatchesAdapter matchesAdapter;
    private ArrayList<Match> matchesList;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_match_history);

        recyclerView = findViewById(R.id.rv_matchHistory);
        recyclerView.setHasFixedSize(true);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        matchesList = new ArrayList<>();

        matchesList.add(new Match("pero", "ivan", "ivan"));
        matchesList.add(new Match("pero", "ivan", "pero"));
        matchesList.add(new Match("iva", "ivan", "ivan"));
        matchesList.add(new Match("ivica", "ivan", "ivica"));
        matchesList.add(new Match("marko", "ivan", "tie"));
        matchesList.add(new Match("petar", "ivan", "ivan"));
        matchesList.add(new Match("ante", "ivan", "tie"));
        matchesList.add(new Match("anto", "ivan", "anto"));
        matchesList.add(new Match("kristijan", "ivan", "ivan"));
        matchesList.add(new Match("pero", "ivan", "tie"));

        matchesList.get(0).addMove(new Move(1, 3));
        matchesList.get(0).addMove(new Move(2, 2));
        matchesList.get(0).addMove(new Move(3, 5));
        matchesList.get(0).addMove(new Move(4, 1));
        matchesList.get(0).addMove(new Move(5, 7));
        matchesList.get(0).addMove(new Move(6, 8));
        matchesList.get(0).addMove(new Move(7, 4));
        matchesList.get(0).addMove(new Move(8, 6));
        matchesList.get(0).addMove(new Move(9, 9));

        matchesAdapter = new MatchesAdapter(MatchHistoryActivity.this, matchesList, this);
        recyclerView.setAdapter(matchesAdapter);
        matchesAdapter.setOnMatchClickListener(MatchHistoryActivity.this);
    }

    @Override
    public void onMatchClick(int position) {
        Intent intent = new Intent(this, MatchDetailsActivity.class);
        Match match = matchesList.get(position);
        intent.putExtra("match", match);

        startActivity(intent);
    }
}