import React from 'react';
import { useRouteMatch } from 'react-router-dom';
import useUserDetail from '../../api/useUserDetail';

export default function User() {
    const match = useRouteMatch();
    const username = match.params.username;
    const user = useUserDetail(username);
    return (
        <div>{user
            ?
            <>
                <h1>{user.username}</h1>
                <img src={user.profile.picture} alt={user.username} />
                <dl>
                    <li> bio</li>
                    <li>{user.profile.bio}</li>
                </dl>
            </>
            :
            <p>Loading...</p>
        }
        </div>
    );
}