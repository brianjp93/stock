import { useEffect } from "react";
import { useMutation } from "react-query";
import { BrowserRouter, Routes, Route, useNavigate } from "react-router-dom";
import { Login } from "./components/auth/login";
import { Home } from './components/home';
import { TickerDetailPage } from './components/stock/tickerDetail';
import { useUserQuery } from "./hooks";
import * as api from "./api/api";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/ticker/:code" element={<TickerDetailPage />} />
      </Routes>
    </BrowserRouter>
  );
}

function Logout() {
  const userQuery = useUserQuery();
  const navigate = useNavigate();

  const logoutMut = useMutation(async () => {
    return api.account.logout().then((data) => {
      userQuery.refetch();
      navigate("/");
      return data;
    });
  });

  useEffect(() => logoutMut.mutate(), [logoutMut]);

  return <div>Logging out...</div>;
}

export default App;
