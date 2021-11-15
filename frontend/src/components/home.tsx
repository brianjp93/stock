import { useUserQuery } from '../hooks'
import { useEffect } from 'react'
import { useNavigate } from 'react-router-dom';

import { Search } from './stock/searchPage'


export function Home() {
  const userQuery = useUserQuery();
  const navigate = useNavigate();

  useEffect(() => {
    if (userQuery.isError) {
      navigate("/login");
    }
  }, [userQuery.isError, navigate]);

  return (
    <>
      {userQuery.isSuccess && <AuthedUserHome user={userQuery.data}/>}
    </>
  )
}

function AuthedUserHome(props: {user: any}) {
  return (
    <>
      <h1>Welcome, {props.user.display_name}</h1>
      <Search />
    </>
  )
}
