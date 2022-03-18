package hr.atos.praksa.tictactoecpp.model;

import java.util.ArrayList;

public class Board {

    private static Board boardInstance;
    private String currentBoardState, previousBoardState;
    private final String emptyBoard = "000000000";
    private int playerMove;

    private Board() {
        currentBoardState = emptyBoard;
        previousBoardState = emptyBoard;
    }

    public static Board getInstance() {
        if (boardInstance == null) {
            boardInstance = new Board();
        }
        return boardInstance;
    }

    public void resetBoard() {
        currentBoardState = emptyBoard;
        previousBoardState = emptyBoard;
    }

    public String getCurrentBoardState() {
        return currentBoardState;
    }

    public void setCurrentBoardState(String currentBoardState) {
        previousBoardState = this.currentBoardState;
        this.currentBoardState = currentBoardState;
    }

    public String getPreviousBoardState() {
        return previousBoardState;
    }

    public void setPreviousBoardState(String previousBoardState) {
        this.previousBoardState = previousBoardState;
    }

    public int getPlayerMove() {
        return playerMove;
    }

    public void setPlayerMove(int playerMove) {
        this.playerMove = playerMove;
    }

}
