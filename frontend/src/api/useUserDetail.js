import { useEffect, useState } from "react";
import fetchUser from "./fetchUser";

export default function useUserDetail(username) {
    const [user, setUser] = useState(null);
    useEffect(() => {
        fetchUser(username).then(user => { setUser(user); });
    }, [username]);
    return user;
}

