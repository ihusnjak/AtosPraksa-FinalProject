package hr.atos.praksa.tictactoe.adapters;

import android.view.View;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import hr.atos.praksa.tictactoe.R;

public class MatchesViewHolder extends RecyclerView.ViewHolder {
    public TextView tvPlayer1, tvPlayer2, tvWinner;
    public MatchesViewHolder(@NonNull View itemView) {
        super(itemView);
        tvPlayer1 = itemView.findViewById(R.id.tv_player1Name);
        tvPlayer2 = itemView.findViewById(R.id.tv_labelPlayer2);
        tvWinner = itemView.findViewById(R.id.tv_Winner);
    }
}
