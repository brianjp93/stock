import axios from 'axios'

const base = '/api/account'

export async function me() {
  const response = await axios.get(`${base}/me/`)
  return response.data
}


export async function logout() {
  return axios.delete(`${base}/logout/`)
}


export async function login(email: string, password: string) {
  const data = {email, password}
  return axios.post(`${base}/login/`, data)
}
