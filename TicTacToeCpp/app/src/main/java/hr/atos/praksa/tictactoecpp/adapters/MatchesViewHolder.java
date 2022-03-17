package hr.atos.praksa.tictactoecpp.adapters;

import android.view.View;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import hr.atos.praksa.tictactoecpp.R;
import hr.atos.praksa.tictactoecpp.listeners.OnMatchClickListener;

public class MatchesViewHolder extends RecyclerView.ViewHolder implements View.OnClickListener {
    public TextView tvPlayer1, tvPlayer2, tvWinner, tvId;
    private OnMatchClickListener listener;

    public MatchesViewHolder(@NonNull View itemView, OnMatchClickListener listener) {
        super(itemView);
        tvPlayer1 = itemView.findViewById(R.id.tv_player1Name);
        tvPlayer2 = itemView.findViewById(R.id.tv_player2Name);
        tvWinner = itemView.findViewById(R.id.tv_Winner);
        tvId = itemView.findViewById(R.id.tv_Id);
        this.listener = listener;

        itemView.setOnClickListener(this);
    }

    @Override
    public void onClick(View view) {
        listener.onMatchClick(getAdapterPosition());
    }
}
