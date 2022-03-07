package hr.atos.praksa.tictactoe.adapters;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;

import hr.atos.praksa.tictactoe.R;
import hr.atos.praksa.tictactoe.model.Match;

public class MatchesAdapter extends RecyclerView.Adapter<MatchesViewHolder> {
    private Context context;
    private ArrayList<Match> matchesTestList;

    public MatchesAdapter(Context context, ArrayList<Match> matchesTestList){
        this.context = context;
        this.matchesTestList = matchesTestList;
    }

    @NonNull
    @Override
    public MatchesViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(context).inflate(R.layout.match_history_item, parent, false);
        return new MatchesViewHolder(v);
    }

    @Override
    public void onBindViewHolder(@NonNull MatchesViewHolder holder, int position) {
        Match currentMatch = matchesTestList.get(position);

        holder.tvPlayer1.setText(currentMatch.getPlayer1());
        holder.tvPlayer2.setText(currentMatch.getPlayer2());
        holder.tvWinner.setText(currentMatch.getWinner());
    }

    @Override
    public int getItemCount() {
        return this.matchesTestList.size();
    }
}
