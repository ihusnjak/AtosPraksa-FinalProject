package hr.atos.praksa.tictactoe.adapters;

import android.view.View;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import hr.atos.praksa.tictactoe.R;
import hr.atos.praksa.tictactoe.listeners.OnMatchClickListener;

public class MatchesViewHolder extends RecyclerView.ViewHolder implements View.OnClickListener {
    public TextView tvPlayer1, tvPlayer2, tvWinner;
    private OnMatchClickListener listener;

    public MatchesViewHolder(@NonNull View itemView, OnMatchClickListener listener) {
        super(itemView);
        tvPlayer1 = itemView.findViewById(R.id.tv_player1Name);
        tvPlayer2 = itemView.findViewById(R.id.tv_labelPlayer2);
        tvWinner = itemView.findViewById(R.id.tv_Winner);
        this.listener = listener;

        itemView.setOnClickListener(this);
    }

    @Override
    public void onClick(View view) {
        listener.onMatchClick(getAdapterPosition());
    }
}
