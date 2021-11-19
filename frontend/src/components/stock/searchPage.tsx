import { useState } from 'react';
import { useMutation } from 'react-query';
import { useForm, Controller, SubmitHandler } from 'react-hook-form';
import Form from "react-bootstrap/Form";
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col'

import { Skeleton } from "../general/skeleton";
import * as api from "../../api/api";

export function SearchPage() {
  return (
    <Skeleton>
      <Search />
    </Skeleton>
  );
}

export function Search() {
  const [data, setData] = useState<[]>([]);

  const onSuccess = (data: any) => {
    setData(data)
  }

  return (
    <>
    <SearchForm onSuccess={onSuccess}/>
    {data.map((item: any) => {
      return (
        <Row>
          <Col>{item.symbol}</Col>
          <Col>{item.description}</Col>
          <Col>{item.displaySymbol}</Col>
          <Col>{item.type}</Col>
        </Row>
      )
    })}
    </>
  );
}

function SearchForm(props: {onSuccess?: (x: any) => void}) {
  const form = useForm<{search: string}>();
  const {errors} = form.formState
  const searchMut = useMutation(
    ['stock-search'],
    (query: string) => api.stock.search(query).then(response => response.result),
    {
      onSuccess: (data) => {
        if (props.onSuccess) {
          props.onSuccess(data)
        }
      },
    }
  )
  const onSubmit: SubmitHandler<{search: string}> = (data) => {
    searchMut.mutate(data.search)
  }

  return (
    <Form onSubmit={form.handleSubmit(onSubmit)}>
      <Form.Group>
        <Form.Label>Search</Form.Label>
        <Controller
          control={form.control}
          name='search'
          rules={{required: true}}
          render={({field}) => {
            return <Form.Control
              {...field}
              type="text"
              placeholder="Search"
            />
        }} />
        {errors.search?.type === 'required' &&
          <small className="text-danger">This field is required.</small>
        }
        <input className='btn btn-success' type='submit' name='Search'/>
      </Form.Group>
    </Form>
  )
}
