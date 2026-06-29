import { useState } from "react";
import api from "../services/api";

export default function Login() {

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const login = async () => {

    try {

      const res = await api.post("login/", {
        username,
        password,
      });

      localStorage.setItem("token", res.data.access);

     window.location.href = "/dashboard";

    } catch (err) {

  console.log(err);

  console.log(err.response);

  alert("Login Failed");

}

  };

  return (

    <div>

      <h1>Login</h1>

      <input
        placeholder="Username"
        onChange={(e)=>setUsername(e.target.value)}
      />

      <br />

      <input
        type="password"
        placeholder="Password"
        onChange={(e)=>setPassword(e.target.value)}
      />

      <br />

      <button onClick={login}>
        Login
      </button>

    </div>

  );

}