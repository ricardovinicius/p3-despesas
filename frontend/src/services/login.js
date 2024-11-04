const axiosRequestConfig = {
  url: import.meta.env.VITE_API_URL
}

export default function login(auth) {
  auth.login({
    url: import.meta.env.VITE_API_URL,
    body: {
      email: "admin@admin.com",
      password: "admin",
    },
    staySignedIn: true,
    fetchUser: true,
  })

  return "hello";
}
