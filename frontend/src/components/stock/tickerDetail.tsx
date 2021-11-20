import { useParams } from 'react-router-dom'
import { useQuery } from 'react-query'
import Card from 'react-bootstrap/Card'

import { Skeleton } from '../general/skeleton';
import * as api from '../../api/api';


export function TickerDetailPage() {
  const params = useParams();
  if (!params.code) {return null}
  return (
    <Skeleton>
      <TickerDetail code={params.code}/>
    </Skeleton>
  )
}

function TickerDetail({code}: {code: string}) {
  const query = useQuery(
    ['basic-financials', code],
    () => api.stock.basicFinancials(code),
    {retry: false, refetchOnWindowFocus: false}
  )
  return (
    <>
      <h1>code</h1>

      {query.isSuccess &&
        <>
          <Card>
            <Card.Body>
              Yoooooo what is up.
            </Card.Body>
          </Card>
        </>
      }
    </>
  )
}
