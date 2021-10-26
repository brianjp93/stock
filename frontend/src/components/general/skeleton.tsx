import Container from 'react-bootstrap/Container'

export function Skeleton(props: any) {
  return (
    <>
      <Container>
        {props.children}
      </Container>
    </>
  )
}
