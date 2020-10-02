import { authFetch } from "../auth";
import { userDetailUrl } from "./endpoints";

export default async function fetchUser(username) {
    const user = await authFetch(userDetailUrl(username)).then(res => {
        if (res.status === 404) {
            return null;
        }
        return res.json();
    });
    return user;
}