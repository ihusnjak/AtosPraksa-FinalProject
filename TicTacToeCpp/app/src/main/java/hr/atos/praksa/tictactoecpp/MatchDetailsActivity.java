package hr.atos.praksa.tictactoecpp;

import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import java.util.ArrayList;

import hr.atos.praksa.tictactoecpp.model.Match;
import hr.atos.praksa.tictactoecpp.model.Move;

public class MatchDetailsActivity extends AppCompatActivity {

    private TextView tvPlayerTurn;
    private Button bNextMove, bPreviousMove;
    private ArrayList<Button> bFieldsList;

    private ArrayList<Move> movesList;
    private int moveNum = 1;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_match_details);

        setupUiElements();
        drawBoard();
    }

    private void setupUiElements(){
        Match match = (Match) getIntent().getSerializableExtra("match");

        tvPlayerTurn = findViewById(R.id.tv_turn);
        tvPlayerTurn.setText(match.getPlayer1());

        bFieldsList = new ArrayList<>();
        bFieldsList.add(findViewById(R.id.b_matchHistory_field1));
        bFieldsList.add(findViewById(R.id.b_matchHistory_field2));
        bFieldsList.add(findViewById(R.id.b_matchHistory_field3));
        bFieldsList.add(findViewById(R.id.b_matchHistory_field4));
        bFieldsList.add(findViewById(R.id.b_matchHistory_field5));
        bFieldsList.add(findViewById(R.id.b_matchHistory_field6));
        bFieldsList.add(findViewById(R.id.b_matchHistory_field7));
        bFieldsList.add(findViewById(R.id.b_matchHistory_field8));
        bFieldsList.add(findViewById(R.id.b_matchHistory_field9));

        for(Button b : bFieldsList){
            b.setEnabled(false);
        }

        movesList = match.getMovesList();

        bNextMove = findViewById(R.id.b_next_move);
        bPreviousMove = findViewById(R.id.b_previous_move);

        bNextMove.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                nextMove();
            }
        });

        bPreviousMove.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                previousMove();
            }
        });
    }

    private void nextMove(){
        if(moveNum < movesList.size()){
            moveNum++;
            drawBoard();
        }
    }

    private void previousMove(){
        if(moveNum > 1){
            moveNum--;
            drawBoard();
        }
    }

    private void drawBoard(){
        clearBoard();
        int playedField = 1;
        for(int i = 0; i < moveNum; i++){
            playedField = movesList.get(i).getPlayedField();
            if((i + 1) % 2 == 0)
                bFieldsList.get(playedField - 1).setText("O");
            else
                bFieldsList.get(playedField - 1).setText("X");
        }
        bFieldsList.get(playedField - 1).setTextColor(Color.RED);
    }

    private void clearBoard(){
        for(TextView tv : bFieldsList){
            tv.setText("");
            tv.setTextColor(Color.WHITE);
        }
    }
}