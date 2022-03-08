package hr.atos.praksa.tictactoe;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    private Button bHumanVsHuman, bHumanVsAi, bAiVsAi, bMatchHistory;

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

        bMatchHistory.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                openMatchHistoryActivity();
            }
        });
    }

    private void openMatchHistoryActivity() {
        Intent intent = new Intent(this, MatchHistoryActivity.class);
        startActivity(intent);
    }
}