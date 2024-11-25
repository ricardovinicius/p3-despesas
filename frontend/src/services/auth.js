export function login(auth, data) {
  auth.login({
      data: {
        email: data.email,
        password: data.password,
      },
      redirect: "/",
      staySignedIn: true,
      fetchUser: true,
    })
}

export function register(auth, data) {
  auth
    .register({
      data: {
        name: data.name,
        email: data.email,
        password: data.password,
      },
      autoLogin: true,
      redirect: "/",
    })
    .catch((error) => {
      if (error.response) {
        console.log(error.response.data);
        console.log(error.response.status);
        console.log(error.response.headers);
      } else if (error.request) {
        console.log(error.request);
      } else {
        console.log("Error", error.message);
      }
      console.log(error.config);
    });
}
