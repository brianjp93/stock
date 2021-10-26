import { useQuery, useMutation } from "react-query";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import { Skeleton } from "./components/general/skeleton";
import Button from "react-bootstrap/Button";
import { Login } from "./components/auth/login";
import * as api from "./api/api";

function App() {
  const userQuery = useQuery("user", api.account.me, {
    refetchOnWindowFocus: false,
    retry: false,
  });

  const logoutMut = useMutation(async () => {
    return api.account.logout().then((data) => {
      userQuery.refetch();
      return data;
    });
  });

  return (
    <div className="App">
      <h1>Welcome!</h1>

      {userQuery.isSuccess && (
        <>
          <div>Hello, {userQuery.data.email}</div>
          <div>
            <Button onClick={() => logoutMut.mutate()}>Logout</Button>
          </div>
        </>
      )}
      {userQuery.isError && <Login />}
    </div>
  );
}

export default App;
