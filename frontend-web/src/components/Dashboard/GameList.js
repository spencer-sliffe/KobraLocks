//Frontend-web/src/components/Dashboard/GameList.js

import React, { useEffect, useState } from 'react';
import { fetchGames } from '../../api';
import './GameList.css'; // We'll define styles here

const GameList = () => {
    const [games, setGames] = useState([]);

    useEffect(() => {
        const getGames = async () => {
            try {
                const gameData = await fetchGames();
                setGames(gameData);
            } catch (error) {
                console.error('Error fetching games:', error);
            }
        };

        getGames();
    }, []);

    return (
        <div className="game-list">
            {games.map(game => (
                <div className="game-card" key={game.id}>
                    <div className="team-names">
                        <div className="team-name">{game.team1}</div>
                        <div className="team-score">{game.team1_score || 0}</div>
                        <div className="team-name">{game.team2}</div>
                        <div className="team-score">{game.team2_score || 0}</div>
                    </div>
                    <div className="odds">
                        <div className="odds-row">
                            <div className="odds-item">Spread</div>
                            <div className="odds-item">{game.team1_spread}</div>
                            <div className="odds-item">{game.team2_spread}</div>
                        </div>
                        <div className="odds-row">
                            <div className="odds-item">Total</div>
                            <div className="odds-item">{game.team1_total}</div>
                            <div className="odds-item">{game.team2_total}</div>
                        </div>
                        <div className="odds-row">
                            <div className="odds-item">Money</div>
                            <div className="odds-item">{game.team1_money}</div>
                            <div className="odds-item">{game.team2_money}</div>
                        </div>
                    </div>
                    {game.live && (
                        <div className="live-info">
                            <span>Live</span> | {game.inning_state}, B: {game.balls}, S: {game.strikes}, O: {game.outs}
                        </div>
                    )}
                </div>
            ))}
        </div>
    );
};

export default GameList;
