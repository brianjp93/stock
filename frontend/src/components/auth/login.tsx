import { useState } from 'react'
import { useMutation, useQuery } from 'react-query'
import * as api from '../../api/api'
import Form from 'react-bootstrap/Form'
import Button from 'react-bootstrap/Button'


export function Login() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  const userQuery = useQuery('user', api.account.me, {retry: false, refetchOnWindowFocus: false})

  const loginMut = useMutation(() => {
    return api.account.login(email, password).then(response => {
      userQuery.refetch()
      return response
    })
  })

  return (
    <>
      <div>
        <Form>
          <Form.Label>Email Address</Form.Label>
          <Form.Control
            type='email'
            placeholder='Enter Email'
            value={email}
            onChange={event => setEmail(event.target.value)}
          />

          <Form.Label>Password</Form.Label>
          <Form.Control
            type='password'
            placeholder='Enter Password'
            value={password}
            onChange={event => setPassword(event.target.value)}
          />
          <Button onClick={() => loginMut.mutate()}>Login</Button>

        </Form>
      </div>
    </>
  )
}
