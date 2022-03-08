package hr.atos.praksa.tictactoe.adapters;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;

import hr.atos.praksa.tictactoe.R;
import hr.atos.praksa.tictactoe.listeners.OnMatchClickListener;
import hr.atos.praksa.tictactoe.model.Match;

public class MatchesAdapter extends RecyclerView.Adapter<MatchesViewHolder> {
    private Context context;
    private ArrayList<Match> matchesList;
    private OnMatchClickListener listener;

    public MatchesAdapter(Context context, ArrayList<Match> matchesTestList, OnMatchClickListener listener){
        this.context = context;
        this.matchesList = matchesTestList;
        this.listener = listener;
    }

    public void setOnMatchClickListener(OnMatchClickListener listener){
        this.listener = listener;
    }

    @NonNull
    @Override
    public MatchesViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(context).inflate(R.layout.match_history_item, parent, false);
        return new MatchesViewHolder(v, listener);
    }

    @Override
    public void onBindViewHolder(@NonNull MatchesViewHolder holder, int position) {
        Match currentMatch = matchesList.get(position);

        holder.tvPlayer1.setText(currentMatch.getPlayer1());
        holder.tvPlayer2.setText(currentMatch.getPlayer2());
        holder.tvWinner.setText(currentMatch.getWinner());
    }

    @Override
    public int getItemCount() {
        return this.matchesList.size();
    }
}
