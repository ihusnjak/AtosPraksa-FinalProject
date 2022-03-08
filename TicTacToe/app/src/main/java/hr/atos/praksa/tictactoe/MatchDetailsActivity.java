package hr.atos.praksa.tictactoe;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;

import hr.atos.praksa.tictactoe.model.Match;

public class MatchDetailsActivity extends AppCompatActivity {

    private TextView tvPlayerTurn;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_match_details);

        Match match = (Match) getIntent().getSerializableExtra("match");

        tvPlayerTurn = findViewById(R.id.tv_turn);
        tvPlayerTurn.setText(match.getPlayer1());

    }
}