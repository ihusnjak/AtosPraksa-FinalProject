package hr.atos.praksa.tictactoecpp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.util.ArrayList;

import hr.atos.praksa.tictactoecpp.model.Match;

public class GameBoardActivity extends AppCompatActivity {

    private ArrayList<Button> bFieldsList;
    private TextView tvPlayerTurn, tvMove;
    private int move = 1;
    private Match match;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_game_board);

        Bundle bundle = getIntent().getExtras();
        int gameType = bundle.getInt("gameType");

        createMatch(bundle, gameType);




        setupUiElements();
    }

    private void createMatch(Bundle bundle, int gameType){
        if(gameType == 1){
            match = new Match(bundle.getString("player1"), bundle.getString("player2"), null);
        }
        else if(gameType == 2){
            int selectedPlayer = bundle.getInt("selectedPlayer");
            if(selectedPlayer == 1){
                match = new Match(bundle.getString("playerName"), "AI", null);
            }
            else if(selectedPlayer == 2){
                match = new Match("AI", bundle.getString("playerName"), null);
            }
        }
        else {
            match = new Match("AI_1", "AI_2", null);
        }
    }

    private void setupUiElements(){
        tvPlayerTurn = findViewById(R.id.tv_match_gameBoard_turn);
        tvMove = findViewById(R.id.tv_gameBoard_move);

        updateMoveAndTurn();

        bFieldsList = new ArrayList<>();
        bFieldsList.add(findViewById(R.id.b_gameBoard_field1));
        bFieldsList.add(findViewById(R.id.b_gameBoard_field2));
        bFieldsList.add(findViewById(R.id.b_gameBoard_field3));
        bFieldsList.add(findViewById(R.id.b_gameBoard_field4));
        bFieldsList.add(findViewById(R.id.b_gameBoard_field5));
        bFieldsList.add(findViewById(R.id.b_gameBoard_field6));
        bFieldsList.add(findViewById(R.id.b_gameBoard_field7));
        bFieldsList.add(findViewById(R.id.b_gameBoard_field8));
        bFieldsList.add(findViewById(R.id.b_gameBoard_field9));

        for(Button btn : bFieldsList){
            btn.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {

                }
            });
        }
    }

    private void updateMoveAndTurn(){
        tvMove.setText("Move: " + move);
        if(move % 2 == 0){
            tvPlayerTurn.setText("Turn: " + match.getPlayer2());
        }
        else {
            tvPlayerTurn.setText("Turn: " + match.getPlayer1());
        }
    }

}