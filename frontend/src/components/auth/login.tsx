import { useMutation } from "react-query";
import { useForm, SubmitHandler } from 'react-hook-form';
import * as api from "../../api/api";
import Form from "react-bootstrap/Form";
import Alert from 'react-bootstrap/Alert';

interface LoginFormType {
  email: string,
  password: string,
}
export function Login() {
  const form = useForm<LoginFormType>();

  const loginMut = useMutation(
    (data: LoginFormType) => api.account.login(data.email, data.password),
    {
      onSuccess: () => {window.location.href = '/'},
    }
  );
  const onSubmit: SubmitHandler<LoginFormType> = (data) => {
    loginMut.mutate(data)
  }

  return (
    <>
      <div>
        {loginMut.isError &&
          <Alert>
            There was an error while trying to log in.
          </Alert>
        }
        <Form onSubmit={form.handleSubmit(onSubmit)}>
          <Form.Label>Email Address</Form.Label>
          <Form.Control
            {...form.register('email', {required: true})}
            type="email"
            placeholder="Enter Email"
          />

          <Form.Label>Password</Form.Label>
          <Form.Control
            {...form.register('password', {required: true})}
            type="password"
            placeholder="Enter Password"
          />
          <input className="btn btn-primary" type="submit" />
        </Form>
      </div>
    </>
  );
}
