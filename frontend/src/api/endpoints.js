const baseUrl = 'http://localhost:8000/';

const loginUrl = `${baseUrl}auth/login/?format=json`;
const logoutUrl = `${baseUrl}auth/logout/?format=json`;
const authUserUrl = `${baseUrl}auth/user/?format=json`;
const timelineUrl = `${baseUrl}timeline/?format=json`;
const postsUrl = `${baseUrl}posts/?format=json`;

const userDetailUrl = (username) => `${baseUrl}users/${username}/?format=json`;

export {
    baseUrl,
    loginUrl,
    logoutUrl,
    timelineUrl,
    authUserUrl,
    postsUrl,
    userDetailUrl
};

