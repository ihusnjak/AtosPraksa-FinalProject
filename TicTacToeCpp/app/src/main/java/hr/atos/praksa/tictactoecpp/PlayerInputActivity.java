package hr.atos.praksa.tictactoecpp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class PlayerInputActivity extends AppCompatActivity {

    private EditText etPlayer1, etPlayer2;
    private Button bSubmit;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_player_input);

        setupUiElements();
    }

    private void setupUiElements(){
        etPlayer1 = findViewById(R.id.et_inputPlayer1);
        etPlayer2 =findViewById(R.id.et_inputPlayer2);
        bSubmit = findViewById(R.id.b_inputPlayerNames);

        bSubmit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                openGameBoardActivity();
            }
        });

    }

    private void openGameBoardActivity(){
        Intent intent = new Intent(this, GameBoardActivity.class);
        startActivity(intent);
    }
}