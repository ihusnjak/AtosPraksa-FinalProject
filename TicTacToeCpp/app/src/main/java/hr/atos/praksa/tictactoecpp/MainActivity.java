package hr.atos.praksa.tictactoecpp;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private Button bHumanVsHuman, bHumanVsAi, bAiVsAi, bMatchHistory;
    static {
        System.loadLibrary("TicTacToe");
    }
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setupUiElements();
    }

    private void setupUiElements(){
        bHumanVsHuman = findViewById(R.id.b_humanVsHuman);
        bHumanVsAi = findViewById(R.id.b_humanVsAi);
        bAiVsAi = findViewById(R.id.b_aiVsAi);
        bMatchHistory = findViewById(R.id.b_matchHistory);

        bHumanVsHuman.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                openPlayerInputActivity();
            }
        });

        bMatchHistory.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                openMatchHistoryActivity();
            }
        });
    }

    private void openPlayerInputActivity(){
        Intent intent = new Intent(this, PlayerInputActivity.class);
        startActivity(intent);
    }

    private void openMatchHistoryActivity() {
        Intent intent = new Intent(this, MatchHistoryActivity.class);
        startActivity(intent);
    }
}