package hr.atos.praksa.tictactoe;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.util.ArrayList;

import hr.atos.praksa.tictactoe.model.Match;
import hr.atos.praksa.tictactoe.model.Move;

public class MatchDetailsActivity extends AppCompatActivity {

    private TextView tvPlayerTurn;
    private Button bNextMove, bPreviousMove;
    private ArrayList<TextView> tvFieldsList;

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

        tvFieldsList = new ArrayList<>();
        tvFieldsList.add(findViewById(R.id.tv_field1));
        tvFieldsList.add(findViewById(R.id.tv_field2));
        tvFieldsList.add(findViewById(R.id.tv_field3));
        tvFieldsList.add(findViewById(R.id.tv_field4));
        tvFieldsList.add(findViewById(R.id.tv_field5));
        tvFieldsList.add(findViewById(R.id.tv_field6));
        tvFieldsList.add(findViewById(R.id.tv_field7));
        tvFieldsList.add(findViewById(R.id.tv_field8));
        tvFieldsList.add(findViewById(R.id.tv_field9));

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
                tvFieldsList.get(playedField - 1).setText("O");
            else
                tvFieldsList.get(playedField - 1).setText("X");
        }
        tvFieldsList.get(playedField - 1).setTextColor(Color.RED);
    }

    private void clearBoard(){
        for(TextView tv : tvFieldsList){
            tv.setText("");
            tv.setTextColor(Color.WHITE);
        }
    }
}