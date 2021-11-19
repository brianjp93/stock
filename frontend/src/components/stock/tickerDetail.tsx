import { useParams } from 'react-router-dom'
import { useQuery } from 'react-query'
import * as api from '../../api/api';


export function TickerDetailPage() {
  const params = useParams();
  if (!params.code) {return}
  return (
    <>
      <TickerDetail code={params.code}/>
    </>
  )
}

function TickerDetail({code}: {code: string}) {
  const basicFinancialsQ = useQuery(
    ['basic-financials', code],
    () => api.stock.basicFinancials(code),
    {retry: false, refetchOnWindowFocus: false}
  )
  return (
    <>
      hello
    </>
  )
}
