export function login(auth, data) {
  auth
    .login({
      url: `${import.meta.env.VITE_API_URL}/user/login`,
      data: {
        email: data.email,
        password: data.password,
      },
      redirect: "/dashboard",
      staySignedIn: true,
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

export function register(auth, data) {
  auth
    .register({
      url: `${import.meta.env.VITE_API_URL}/user`,
      data: {
        name: data.name,
        email: data.email,
        password: data.password,
      },
      autoLogin: false,
      redirect: "/login",
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
