// frontend-web/src/components/Dashboard/Home/Home.js
import React, { useState } from 'react';
import NCAABBSchedule from './Schedule/NCAABBSchedule'; // NCAA Baseball Schedule
import MLBSchedule from './Schedule/MLBSchedule'; // MLB Schedule
import MLSSchedule from './Schedule/MLSSchedule'; // MLS Schedule
import NBASchedule from './Schedule/NBASchedule'; // NBA Schedule
import NCAAFBSchedule from './Schedule/NCAAFBSchedule'; // NCAA Football Schedule
import NFLSchedule from './Schedule/NFLSchedule'; // NFL Schedule
import WNBASchedule from './Schedule/WNBASchedule'; // WNBA Schedule
import {
  LeagueNav,
  LeagueNavContainer,
  LeagueNavMenu,
  LeagueNavItem,
  LeagueNavLinks,
} from './HomeElements';
import './Home.css';

const Home = () => {
    const [selectedLeague, setSelectedLeague] = useState('NFL'); // Default to NFL

    const renderSchedule = () => {
        switch (selectedLeague) {
            case 'NCAABB':
                return <NCAABBSchedule />;
            case 'MLB':
                return <MLBSchedule />;
            case 'MLS':
                return <MLSSchedule />;
            case 'NBA':
                return <NBASchedule />;
            case 'NCAAFB':
                return <NCAAFBSchedule />;
            case 'NFL':
                return <NFLSchedule />;
            case 'WNBA':
                return <WNBASchedule />;
            default:
                return <NBASchedule />;
        }
    };

    return (
        <div>
            <LeagueNav>
                <LeagueNavContainer>
                    <LeagueNavMenu>
                        <LeagueNavItem>
                            <LeagueNavLinks
                                to="#"
                                onClick={() => setSelectedLeague('NCAABB')}
                                className={selectedLeague === 'NCAABB' ? 'active' : ''}
                            >
                                NCAA BB
                            </LeagueNavLinks>
                        </LeagueNavItem>
                        <LeagueNavItem>
                            <LeagueNavLinks
                                to="#"
                                onClick={() => setSelectedLeague('MLB')}
                                className={selectedLeague === 'MLB' ? 'active' : ''}
                            >
                                MLB
                            </LeagueNavLinks>
                        </LeagueNavItem>
                        <LeagueNavItem>
                            <LeagueNavLinks
                                to="#"
                                onClick={() => setSelectedLeague('MLS')}
                                className={selectedLeague === 'MLS' ? 'active' : ''}
                            >
                                MLS
                            </LeagueNavLinks>
                        </LeagueNavItem>
                        <LeagueNavItem>
                            <LeagueNavLinks
                                to="#"
                                onClick={() => setSelectedLeague('NBA')}
                                className={selectedLeague === 'NBA' ? 'active' : ''}
                            >
                                NBA
                            </LeagueNavLinks>
                        </LeagueNavItem>
                        <LeagueNavItem>
                            <LeagueNavLinks
                                to="#"
                                onClick={() => setSelectedLeague('NCAAFB')}
                                className={selectedLeague === 'NCAAFB' ? 'active' : ''}
                            >
                                NCAA FB
                            </LeagueNavLinks>
                        </LeagueNavItem>
                        <LeagueNavItem>
                            <LeagueNavLinks
                                to="#"
                                onClick={() => setSelectedLeague('NFL')}
                                className={selectedLeague === 'NFL' ? 'active' : ''}
                            >
                                NFL
                            </LeagueNavLinks>
                        </LeagueNavItem>
                        <LeagueNavItem>
                            <LeagueNavLinks
                                to="#"
                                onClick={() => setSelectedLeague('WNBA')}
                                className={selectedLeague === 'WNBA' ? 'active' : ''}
                            >
                                WNBA
                            </LeagueNavLinks>
                        </LeagueNavItem>
                    </LeagueNavMenu>
                </LeagueNavContainer>
            </LeagueNav>
            <div className="schedule-content">
                {renderSchedule()}
            </div>
        </div>
    );
};

export default Home;

