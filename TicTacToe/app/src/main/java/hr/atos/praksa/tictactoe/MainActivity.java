package hr.atos.praksa.tictactoe;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    private Button b_humanVsHuman, b_humanVsAi, b_aiVsAi, b_matchHistory;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setupUiElements();
    }

    private void setupUiElements(){
        b_humanVsHuman = findViewById(R.id.b_humanVsHuman);
        b_humanVsAi = findViewById(R.id.b_humanVsAi);
        b_aiVsAi = findViewById(R.id.b_humanVsAi);
        b_matchHistory = findViewById(R.id.b_matchHistory);

        b_matchHistory.setOnClickListener(new View.OnClickListener() {
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