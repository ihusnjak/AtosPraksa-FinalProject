package hr.atos.praksa.tictactoecpp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.Toast;

public class PlayerAiInputActivity extends AppCompatActivity {

    EditText etPlayerName;
    Button bSubmit;
    RadioGroup rgPlayerSelect;
    RadioButton rbSelectPlayer1, rbSelectPlayer2;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_player_ai_input);

        setupUiElements();
    }

    private void setupUiElements(){
        etPlayerName = findViewById(R.id.et_inputPlayerName);
        bSubmit = findViewById(R.id.b_inputPlayerName);
        rgPlayerSelect = findViewById(R.id.rg_playerSelect);
        rbSelectPlayer1 = findViewById(R.id.rb_selectPlayer1);
        rbSelectPlayer2 = findViewById(R.id.rb_selectPlayer2);

        rgPlayerSelect.check(rbSelectPlayer1.getId());

        bSubmit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                openGameBoardActivity();
            }
        });
    }

    private void openGameBoardActivity() {
        if (!TextUtils.isEmpty(etPlayerName.getText().toString())) {
            Intent intent = new Intent(this, GameBoardActivity.class);
            Bundle bundle = new Bundle();
            bundle.putString("playerName", etPlayerName.getText().toString());
            bundle.putInt("gameType", 2);
            if(rbSelectPlayer1.isChecked()){
                bundle.putInt("selectedPlayer", 1);
            }
            else if(rbSelectPlayer2.isChecked()){
                bundle.putInt("selectedPlayer", 2);
            }

            intent.putExtras(bundle);
            startActivity(intent);
        }
        else {
            Toast.makeText(getApplicationContext(), "Please fill in player name field.", Toast.LENGTH_SHORT).show();
        }

    }
}