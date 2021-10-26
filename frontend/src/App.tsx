import { useQuery, useMutation } from 'react-query'
import Button from 'react-bootstrap/Button'
import { Login } from './components/auth/login'
import * as api from './api/api'


function App() {

  const userQuery = useQuery(
    'user',
    api.account.me,
    {refetchOnWindowFocus: false, retry: false}
  )

    const logoutMut = useMutation(async () => {
      return api.account.logout().then(data => {
        userQuery.refetch()
        return data
      })
    })

  return (
      <div className="App">
        <header className="App-header">
          <h1>Welcome!</h1>

          {userQuery.isSuccess &&
            <>
              <div>
                Hello, {userQuery.data.email}
              </div>
              <div>
                <Button onClick={() => logoutMut.mutate()}>
                  Logout
                </Button>
              </div>
            </>
          }
          {userQuery.isError &&
            <Login />
          }
        </header>
      </div>
  );
}

export default App;
