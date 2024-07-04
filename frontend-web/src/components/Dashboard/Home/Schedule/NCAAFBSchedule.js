//Frontend-web/src/components/Dashboard/NCAAFBSchedule.js

import React, { useEffect, useState } from 'react';
import { fetchNCAAFBGames } from '../../../../api';
import './GameSchedule.css'; // We'll define styles here

const NCAAFBSchedule = () => {
    const [games, setGames] = useState([]);

    useEffect(() => {
        const getGames = async () => {
            try {
                const gameData = await fetchNCAAFBGames();
                setGames(gameData);
            } catch (error) {
                console.error('Error fetching games:', error);
            }
        };

        getGames();
    }, []);
    const formatOdds = (odds) => {
        const [value, line] = odds.split(' ');
        return (
            <div className="odds">
                <span>{value}</span>
                <span>{line}</span>
            </div>
        );
    };

    const formatTotal = (total) => {
        const [indicator, value, odds] = total.split(' ');
        return (
            <div className="total-wrapper">
                <div className="total-indicator">{indicator} {value}</div>
                <div className="total-odds">{odds}</div>
            </div>
        );
    };

    return (
        <div className="game-list">
            {games.map(game => (
                <div className="game-card" key={game.id}>
                    <div className="header-row">
                        <div className="schedule-info">{game.live ? 'LIVE' : game.game_time}</div>
                        <div className="odds-column-name">Spread</div>
                        <div className="odds-column-name">Total</div>
                        <div className="odds-column-name">Money</div>
                    </div>
                    <div className="team-row">
                        <div className="team-name-and-score">{game.team1} {game.team1_score || ''}</div>
                        <div className="spread-column">{formatOdds(game.team1_spread)}</div>
                        <div className="total-column">{formatTotal(game.team1_total)}</div>
                        <div className="money-column">{game.team1_money}</div>
                    </div>
                    <div className="team-row">
                        <div className="team-name-and-score">{game.team2} {game.team2_score || ''}</div>
                        <div className="spread-column">{formatOdds(game.team2_spread)}</div>
                        <div className="total-column">{formatTotal(game.team2_total)}</div>
                        <div className="money-column">{game.team2_money}</div>
                    </div>
                    {game.live && (
                        <div className="live-info">
                            <span>Live</span> | {game.quarter_state}: {game.clock}
                        </div>
                    )}
                </div>
            ))}
        </div>
    );
};

export default NCAAFBSchedule;
