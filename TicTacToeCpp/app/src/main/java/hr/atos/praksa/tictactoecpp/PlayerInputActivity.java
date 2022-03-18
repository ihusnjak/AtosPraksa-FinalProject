package hr.atos.praksa.tictactoecpp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class PlayerInputActivity extends AppCompatActivity {

    private EditText etPlayer1, etPlayer2;
    private Button bSubmit;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_player_input);

        setupUiElements();
    }

    private void setupUiElements() {
        etPlayer1 = findViewById(R.id.et_inputPlayer1);
        etPlayer2 = findViewById(R.id.et_inputPlayer2);
        bSubmit = findViewById(R.id.b_inputPlayerNames);

        bSubmit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                openGameBoardActivity();
            }
        });

    }

    private void openGameBoardActivity() {
        if (!TextUtils.isEmpty(etPlayer1.getText().toString())
                && !TextUtils.isEmpty(etPlayer2.getText().toString())) {
            Intent intent = new Intent(this, GameBoardActivity.class);
            Bundle bundle = new Bundle();
            bundle.putString("player1", etPlayer1.getText().toString());
            bundle.putString("player2", etPlayer2.getText().toString());
            bundle.putInt("gameType", 1);
            intent.putExtras(bundle);
            startActivity(intent);
        }
        else {
            Toast.makeText(getApplicationContext(), "Please fill in both fields.", Toast.LENGTH_SHORT).show();
        }

    }
}