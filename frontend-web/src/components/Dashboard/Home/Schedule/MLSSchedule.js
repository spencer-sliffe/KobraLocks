//Frontend-web/src/components/Dashboard/MLSSchedule.js

import React, { useEffect, useState } from 'react';
import { fetchMLSGames } from '../../../../api';
import './GameSchedule.css'; // We'll define styles here

const MLSSchedule = () => {
    const [games, setGames] = useState([]);

    useEffect(() => {
        const getGames = async () => {
            try {
                const gameData = await fetchMLSGames();
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
                    {!game.live && (
                        <div className="schedule-info">
                            {game.game_time}
                        </div>
                    )}
                    <div className="team-names">
                        <div className="team-name">{game.team1} | {game.team1_record}</div>
                        <div className="team-score">{game.team1_score || 'TBD'}</div>
                        <div className="team-name">{game.team2} | {game.team2_record}</div>
                        <div className="team-score">{game.team2_score || 'TBD'}</div>
                    </div>
                    <div className="odds">
                        <div className="odds-row">
                            <div className="odds-item">{game.team1}</div>
                            <div className="odds-item">{game.team1_odds}</div>
                        </div>
                        <div className="odds-row">
                            <div className="odds-item">Draw</div>
                            <div className="odds-item">{game.draw_odds}</div>
                        </div>
                        <div className="odds-row">
                            <div className="odds-item">{game.team2}</div>
                            <div className="odds-item">{game.team2_odds}</div>
                        </div>
                    </div>
                    {game.live && (
                        <div className="live-info">
                            <span>Live</span> | {game.clock}
                        </div>
                    )}
                </div>
            ))}
        </div>
    );
};

export default MLSSchedule;
